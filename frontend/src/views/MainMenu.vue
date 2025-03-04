<template>
    <div class="flex flex-col items-center justify-center h-screen text-center">
      <h1 class="text-2xl font-semibold mb-6">Welcome to the Main Menu</h1>
      <button
        class="hover:cursor-pointer rounded-lg bg-red-500 text-white py-2 px-4"
        type="button"
        @click="logout"
      >
        Logout
      </button>
    </div>
  </template>
  
  <script setup lang="ts">
  import { useRouter } from 'vue-router';
  import { removeToken } from '../api/api.ts';
  
  const router = useRouter();
  
  const logout = () => {
    removeToken();
    router.push('/login');
  };
  </script>
  