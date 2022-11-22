<script setup lang="ts">
import type { AxiosStatic } from 'axios';
import TaskList from '@/components/TaskList.vue';
import { inject, onMounted, ref } from 'vue';
import AddTask from '@/components/AddTask.vue';

const tasks = ref([]);
const loading = ref(true);

const axios = inject('axios') as AxiosStatic;

async function getTasks() {
  return axios.get('todo/').then((r) => {
    tasks.value = r.data;
  });
}

function refreshTasks() {
  loading.value = true;

  getTasks().then(() => {
    loading.value = false;
  });
}
onMounted(() => {
  getTasks().then(() => {
    loading.value = false;
  });
});
</script>

<template>
  <main class="container">
    <div class="d-flex justify-content-end my-4">
      <button
        class="btn btn-primary btn-rounded"
        data-mdb-toggle="modal"
        data-mdb-target="#AddTask"
      >
        Add task
      </button>
    </div>
    <TaskList :tasks="tasks" @refresh-todo="refreshTasks" />
  </main>

  <AddTask @task-add="refreshTasks" />
</template>
