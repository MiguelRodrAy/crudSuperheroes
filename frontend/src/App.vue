<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { getToken } from './api/api.ts';

const router = useRouter();

if (getToken()) {
  router.push('/menu');
}
</script>
