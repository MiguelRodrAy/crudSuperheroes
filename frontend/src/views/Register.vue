<template>
    <div class="register flex items-center justify-center h-screen bg-gray-100">
      <div class="bg-white p-8 rounded-lg shadow-lg max-w-sm w-full">
        <h2 class="text-2xl font-semibold text-center mb-6">Register</h2>
        <form @submit.prevent="registerUser">
          <div class="mb-4">
            <input
              v-model="username"
              type="text"
              placeholder="Username"
              required
              class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div class="mb-4">
            <input
              v-model="email"
              type="email"
              placeholder="Email"
              required
              class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>


          <div class="mb-6">
            <input
              v-model="password"
              type="password"
              placeholder="Password"
              required
              class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          
          <button
            type="submit"
            class="w-full py-3 bg-blue-500 text-white font-semibold rounded-md hover:bg-blue-600 transition duration-200"
          >
            Register
          </button>

          <p class="mt-4 text-center">
          Already have an account? <router-link to="/login" class="text-blue-500">Log In</router-link>
        </p>
        </form>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { register, setToken } from '../api/api.ts';
  import { useRouter } from 'vue-router';
  
  const username = ref('');
  const password = ref('');
  const email = ref('');
  const router = useRouter();
  
  const registerUser = async () => {
    try {
      const response = await register(username.value, password.value, email.value);
      setToken(response.token);
      router.push('/login'); 
      console.log('Registration successful', response);
    } catch (error) {
      console.error('Registration failed', error);
    }
  };
  </script>
  