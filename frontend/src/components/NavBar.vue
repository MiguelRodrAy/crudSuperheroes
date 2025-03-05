<template>
  <nav class="w-full bg-gray-100 shadow-md px-6 py-3 flex items-center justify-between">
    <div class="text-lg font-semibold">SuperHeroes App</div>

    <div class="flex items-center space-x-4">
      <span class="font-medium">{{ username }}</span>
      <button
        class="hover:cursor-pointer rounded-lg bg-red-500 text-white py-2 px-4"
        type="button"
        @click="logout"
      >
        Logout
      </button>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { removeToken, removeUsername, getUsername } from '../api/api.ts';

const username = ref<string | null>(null);

const router = useRouter();

onMounted(() => {
  username.value = getUsername();
});

const logout = () => {
  removeToken();
  removeUsername();
  router.push('/login');
};
</script>
