<template>
    <div class="login flex items-center justify-center h-screen bg-gray-100">
      <div class="bg-white p-8 rounded-lg shadow-lg max-w-sm w-full">
        <h2 class="text-2xl font-semibold text-center mb-6">Login</h2>
        <form @submit.prevent="loginUser">
          <div class="mb-4">
            <input
              v-model="username"
              type="text"
              placeholder="Username"
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
            Login
          </button>
        </form>
        <p class="mt-4 text-center">
          Don't have an account? <router-link to="/register" class="text-blue-500">Register</router-link>
        </p>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { login, setToken, setUsername } from '../api/api.ts';
  import { useRouter } from 'vue-router';
  
  const username = ref('');
  const password = ref('');
  const router = useRouter();
  
  const loginUser = async () => {
    try {
      const response = await login(username.value, password.value);
      setToken(response.token);
      setUsername(response.username);
      router.push('/menu');
      console.log('Login successful', response);
    } catch (error) {
      console.error('Login failed', error);
    }
  };
  </script>
  