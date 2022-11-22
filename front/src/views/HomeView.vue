<script setup lang="ts">
import type { AxiosStatic } from 'axios';
import TaskList from '@/components/TaskList.vue';
import { inject, onMounted, ref } from 'vue';
import AddTask from '@/components/AddTask.vue';

const tasks = ref([]);
const loading = ref(true);
const filter = ref('all');

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

function filterTasks() {
  if (filter.value == 'completed') {
    return axios.get('todo?completed=true').then((r) => {
      tasks.value = r.data;
    });
  } else if (filter.value == 'pending') {
    return axios.get('todo?pending=true').then((r) => {
      tasks.value = r.data;
    });
  } else {
    return axios.get('todo/').then((r) => {
      tasks.value = r.data;
    });
  }
}

onMounted(() => {
  getTasks().then(() => {
    loading.value = false;
  });
});
</script>

<template>
  <main class="container">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Filters</h5>

        <div class="d-flex gap-2">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="filterRadios"
              id="all"
              value="all"
              v-model="filter"
            />
            <label class="form-check-label" for="all"> All </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="filterRadios"
              id="completed"
              value="completed"
              v-model="filter"
            />
            <label class="form-check-label" for="completed"> Completed </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="filterRadios"
              id="pending"
              value="pending"
              v-model="filter"
            />
            <label class="form-check-label" for="pending"> Pending </label>
          </div>
        </div>

        <button
          type="button"
          class="btn btn-primary btn-sm btn-rounded mt-3"
          @click="filterTasks"
        >
          submit
        </button>
      </div>
    </div>

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
