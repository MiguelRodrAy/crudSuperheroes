<template>
  <div class="h-screen flex flex-col">
    <NavBar />
    <div class="flex-1 flex flex-col items-center justify-start text-center p-6 bg-blue-300">
      <h1 class="text-2xl font-semibold mb-4">Superheroes Collection</h1>
      <div class="flex items-center justify-center space-x-4 mb-6">
        <div class="flex-1 mx-6">
          <input
            type="text"
            placeholder="Search in collection..."
            class="w-full max-w-lg px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
            v-model="searchQuery"
          />
        </div>
        <button
          class="px-4 py-2 bg-green-500 text-white font-semibold rounded-lg hover:bg-green-400 transition-all"
          @click="addModal"
        >
          Add
        </button>
      </div>

      <div v-if="isModalOpen" class="fixed inset-0 bg-opacity-10 flex justify-center items-center z-50 backdrop-blur-lg">
        <div class="bg-gray-100 p-8 rounded-lg w-96">
          <h2 class="text-2xl font-semibold mb-4">{{ isEditing ? 'Edit Superhero' : 'Add Superhero' }}</h2>

          <form @submit.prevent="submitForm">
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Alias</label>
              <input
                type="text"
                v-model="newHero.name"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg"
                required
              />
            </div>

            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Name</label>
              <input
                type="text"
                v-model="newHero.lastName"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg"
                required
              />
            </div>

            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Super Powers</label>

              <div class="flex flex-col">
                <div v-if="isAddingNewSuperPower">
                  <div class="relative w-full">
                    <input
                      v-model="newSuperPower"
                      type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-lg pr-10"
                      placeholder="Add new superpower"
                    />
                    <button
                      type="button"
                      @click="cancelAddNewSuperPower"
                      class="absolute right-2 top-1/2 transform -translate-y-1/2 text-red-500"
                    >
                      ✖
                    </button>
                  </div>
                </div>

                <div v-else>
                  <select
                    v-model="selectedSuperPower"
                    class="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    @change="handleSuperpowerSelect"
                  >
                    <option value="0">Add new superpower</option>
                    <option v-for="power in superPowers" :key="power.id" :value="power.id">
                      {{ power.name }}
                    </option>
                  </select>
                </div>
              </div>

              <button
                v-if="isAddingNewSuperPower"
                type="button"
                @click="addSuperPower()"
                class="my-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:cursor-pointer"
              >
                Add
              </button>

              <div v-if="selectedSuperPowers.length" class="mt-4">
                <p class="font-semibold">Selected Superpowers:</p>
                <ul>
                  <li v-for="(power, index) in selectedSuperPowers" :key="index" class="flex justify-between items-center p-1 px-2 my-2 rounded-xl border-gray-600 border-1">
                    <span>{{ power.name }}</span>
                    <button
                      type="button"
                      @click="removeSuperPower(index)"
                      class="ml-2 text-red-500"
                    >
                      ✖
                    </button>
                  </li>
                </ul>
              </div>
            </div>

            <div class="my-4">
              <label class="block text-sm font-medium text-gray-700">League</label>

              <div v-if="isAddingNewLeague">
                <div class="relative w-full">
                  <input
                    v-model="newLeagueName"
                    type="text"
                    class="w-full px-3 py-2 border border-gray-300 rounded-lg pr-10"
                    placeholder="Add new league"
                  />
                  <button
                    type="button"
                    @click="cancelAddNewLeague"
                    class="absolute right-2 top-1/2 transform -translate-y-1/2 text-red-500"
                  >
                    ✖
                  </button>
                </div>

                <button
                  type="button"
                  @click="addLeague"
                  class="my-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:cursor-pointer"
                >
                  Add League
                </button>
              </div>

              <div v-else>
                <select
                  v-model="selectedLeague"
                  class="w-full px-3 py-2 border border-gray-300 rounded-lg"
                  @change="handleLeagueSelect"
                >
                  <option value="0">Add new league</option>
                  <option v-for="league in leagues" :key="league.id" :value="league.id">
                    {{ league.name }}
                  </option>
                </select>
              </div>
            </div>

            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Hero Image</label>
              <input
                type="file"
                @change="onFileChange"
                accept="image/*"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg"
              />
              
              <div v-if="imageUrl" class="mt-2 items-center flex flex-col">
                <p class="text-sm text-gray-500">Preview:</p>
                <img :src="imageUrl" alt="Hero Image Preview" class="w-40 h-40 object-cover rounded-lg mt-2"/>
              </div>
            </div>

            <div class="flex justify-between">
              <button
                type="button"
                @click="closeModal"
                class="px-4 py-2 bg-gray-300 text-gray-700 rounded-lg"
              >
                Cancel
              </button>
              <button
                type="submit"
                class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:cursor-pointer"
              >
              {{ isEditing ? 'Confirm' : 'Add' }}
              </button>
            </div>
          </form>

        </div>
      </div>

      <div class="w-full max-w-4xl grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="hero in filteredSuperheroes" :key="hero.id" class="relative group flex items-center justify-center">
          <div class=" h-100 w-full max-w-70 overflow-hidden rounded-lg shadow-lg bg-white">
            <img
              :src="'http://127.0.0.1:8000/Photos/' + hero.name.toLowerCase().replace(/\s+/g, '') + '.png'"
              :alt="hero.name"
              class="h-full w-full object-cover transition-transform transform group-hover:scale-105"
            />
          </div>

          <div class="absolute inset-0 bg-gradient-to-r from-red-500 via-purple-500 to-blue-500 text-white flex flex-col items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity rounded-lg">
            <p class="mt-2 text-lg font-bold uppercase">{{ hero.name }}</p>
            <p class="text-xl font-semibold">{{ hero.lastName }}</p>
            <p class="mt-2 text-sm">League: {{ hero.league ? hero.league.name : 'No league' }}</p>
            <div class="mt-2 text-sm">
              <p>Skills:</p>
              <div class="flex flex-wrap justify-center gap-2">
                <span
                  v-for="(skill, index) in hero.superPowers"
                  :key="index"
                  class="bg-gray-200 text-gray-800 py-1 px-3 rounded-lg"
                >
                  {{ skill.name }}
                </span>
              </div>
            </div>
            <div class="mt-4 w-1/2 flex  flex-col justify-center">
              <button
                class="px-4 py-2 mt-10 text-gray-900 bg-white font-semibold rounded-lg hover:bg-gray-200 transition-all hover:cursor-pointer"
                @click="editModal(hero)"
              >
                Edit
              </button>

              <button
                class="px-4 py-2 mt-10 text-white bg-red-500 font-semibold rounded-lg hover:bg-red-600 transition-all hover:cursor-pointer"
                @click="deleteHero(hero.id)"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import NavBar from '../components/NavBar.vue';

interface SuperPower {
  id: number;
  name: string;
}

interface League {
  id: number;
  name: string;
}

interface Superhero {
  id: number;
  name: string;
  lastName: string;
  superPowers: SuperPower[];
  league: League | null;
}

const imageUrl = ref<string | null>(null);
const selectedImage = ref<File | null>(null);
const searchQuery = ref('');
const isModalOpen = ref(false);
const newHero = ref<Superhero>({
  id: 0,
  name: '',
  lastName: '',
  superPowers: [],
  league: null,
});
const selectedSuperPowers = ref<SuperPower[]>([]);
const selectedLeague = ref<number | null>(null);
const newSuperPower = ref('');
const isAddingNewSuperPower = ref(false);
const isAddingNewLeague = ref(false);
const isEditing = ref(false);
const newLeagueName = ref('');
const selectedSuperPower = ref<number | null>(null);

const superheroes = ref<Superhero[]>([]);
const superPowers = ref<SuperPower[]>([]);
const leagues = ref<League[]>([]);
const selectedSuperPowersList = ref<{ id: number; name: string }[]>([]);

const fetchSuperheroes = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/superheroes/');
    superheroes.value = await response.json();
  } catch (error) {
    console.error('Error fetching superheroes:', error);
  }
};

const fetchSuperpowers = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/superpowers');
    superPowers.value = await response.json();
  } catch (error) {
    console.error('Error fetching superpowers:', error);
  }
};

const fetchLeagues = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/leagues');
    leagues.value = await response.json();
  } catch (error) {
    console.error('Error fetching leagues:', error);
  }
};

onMounted(() => {
  fetchSuperheroes();
  fetchSuperpowers();
  fetchLeagues();
});

const filteredSuperheroes = computed(() => {
  const searchTerm = searchQuery.value.toLowerCase();
  return superheroes.value.filter(hero =>
    hero.name.toLowerCase().includes(searchTerm) || hero.lastName.toLowerCase().includes(searchTerm)
  );
});


const addModal = () => {
  resetForm();
  isEditing.value = false;
  isModalOpen.value = true;
};

const editModal = (hero: Superhero) => {
  newHero.value = { ...hero };
  selectedSuperPowers.value = [...hero.superPowers];
  selectedLeague.value = hero.league?.id ?? null;
  isEditing.value = true;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};

const handleSuperpowerSelect = () => {
  if (selectedSuperPower.value === "0") {
    isAddingNewSuperPower.value = true;
  } else {
    isAddingNewSuperPower.value = false;
    const power = superPowers.value.find(p => p.id === selectedSuperPower.value);
    if (power && !selectedSuperPowers.value.some(p => p.id === power.id)) {
      selectedSuperPowers.value.push(power);
    }
  }
};


const handleLeagueSelect = () => {
  if (selectedLeague.value === "0") {
    isAddingNewLeague.value = true;
  } else {
    isAddingNewLeague.value = false;
  }
};

const addLeague = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/leagues/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: newLeagueName.value.trim() }),
    });
    const createdLeague = await response.json();
    leagues.value.push(createdLeague);
    selectedLeague.value = createdLeague.league.id;
    isAddingNewLeague.value = false;
    newLeagueName.value = '';
  } catch (error) {
    console.error('Error adding new league:', error);
  }
};

const cancelAddNewLeague = () => {
  isAddingNewLeague.value = false;
  newLeagueName.value = '';
};

const addSuperPower = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/superpowers/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: newSuperPower.value.trim() }),
    });
    const createdPower = await response.json();
    superPowers.value.push(createdPower);
    selectedSuperPowers.value.push(createdPower.superpower);
    isAddingNewSuperPower.value = false;
    newSuperPower.value = '';
  } catch (error) {
    console.error('Error adding new superpower:', error);
  }
};

const removeSuperPower = (index: number) => {
  selectedSuperPowers.value.splice(index, 1);
};

const cancelAddNewSuperPower = () => {
  isAddingNewSuperPower.value = false;
  newSuperPower.value = '';
};

const submitForm = async () => {
  const selectedLeagueObj = leagues.value.find(l => l.id === selectedLeague.value) || null;

  const newHeroPayload = {
    name: newHero.value.name,
    lastName: newHero.value.lastName,
    superPowers: selectedSuperPowers.value.map(power => ({ id: power.id, name: power.name })),
    league: selectedLeagueObj,
  };

  try {
    let response;
    if (isEditing.value) {
      response = await fetch(`http://127.0.0.1:8000/superheroes/${newHero.value.id}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newHeroPayload),
      });
    } else {
      response = await fetch('http://127.0.0.1:8000/superheroes/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newHeroPayload),
      });
    }

    const result = await response.json();
    if (isEditing.value) {
      const index = superheroes.value.findIndex(hero => hero.id === result.id);
      if (index !== -1) {
        superheroes.value[index] = result;
      }
    } else {
      superheroes.value.push(result);
    }

    if (selectedImage.value) {
      const newFileName = `${newHero.value.name.toLowerCase().replace(/\s+/g, '')}.png`;
      const renamedFile = new File([selectedImage.value], newFileName, { type: selectedImage.value.type });
      const formData = new FormData();
      formData.append('file', renamedFile);
      await fetch(`http://127.0.0.1:8000/superhero/SaveFile`, {
        method: 'POST',
        body: formData,
      });
    }

    location.reload();
    closeModal();
  } catch (error) {
    console.error('Error submitting form:', error);
  }
};



const resetForm = () => {
  newHero.value = { id: 0, name: '', lastName: '', superPowers: [], league: null };
  selectedSuperPowers.value = [];
  selectedLeague.value = null;
  isAddingNewSuperPower.value = false;
  newSuperPower.value = '';
  selectedSuperPower.value = null;
};

const deleteHero = async (id: number) => {
  try {
    await fetch('http://127.0.0.1:8000/superheroes/' + id + '/', {
      method: 'DELETE',
    });
    superheroes.value = superheroes.value.filter(hero => hero.id !== id);
  } catch (error) {
    console.error('Error deleting superhero:', error);
  }
};

const onFileChange = (event: Event) => {
  const input = event.target as HTMLInputElement;
  selectedImage.value = input.files?.[0] ?? null;

  if (selectedImage.value) {
    const reader = new FileReader();
    reader.onload = () => {
      imageUrl.value = reader.result as string;
    };
    reader.readAsDataURL(selectedImage.value);
  }
};
</script>

