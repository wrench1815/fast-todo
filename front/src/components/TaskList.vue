<script setup lang="ts">
import { inject } from 'vue';
import type { AxiosStatic } from 'axios';
const axios = inject('axios') as AxiosStatic;

const props = defineProps<{
  tasks: Array<{
    id: number;
    task: string;
    is_completed: boolean;
    date_added: string;
  }>;
}>();

const emit = defineEmits(['refresh-todo']);

function formattedDate(inputDate: string) {
  const date = new Date(inputDate);
  return `${date.toLocaleString('default', {
    weekday: 'short',
  })}, ${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`;
}

function markDone(id: number) {
  return axios.get(`todo/${id}/complete`).then((r) => {
    if (r.status == 200) {
      emit('refresh-todo');
    }
  });
}

function deleteTask(id: number) {
  return axios.delete(`todo/${id}`).then((r) => {
    if (r.status == 200) {
      emit('refresh-todo');
    }
  });
}
</script>

<template>
  <div class="card card-bod">
    <div class="table-responsive">
      <table class="table table-borderless align-middle">
        <thead class="bg-primary text-white fs-6">
          <tr>
            <th scope="col">Id</th>
            <th scope="col">Task</th>
            <th scope="col">status</th>
            <th scope="col" class="text-nowrap">Date added</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody v-if="tasks.length != 0">
          <tr v-for="task in tasks" :key="task.id">
            <td>{{ task.id }}</td>
            <td class="">{{ task.task }}</td>
            <td class="text-nowrap">
              <div
                v-if="task.is_completed"
                class="d-flex align-items-center gap-1 text-success fw-bold"
              >
                <i class="ri-check-fill fs-5"></i>done
              </div>
              <div
                v-else
                class="d-flex align-items-center gap-1 text-warning fw-bold"
              >
                <i class="ri-error-warning-line fs-5"></i>pending
              </div>
            </td>
            <td class="text-nowrap">{{ formattedDate(task.date_added) }}</td>
            <td>
              <div class="d-flex gap-2">
                <button
                  class="btn btn-rounded btn-floating text-info d-flex align-items-center justify-content-center"
                  @click="markDone(task.id)"
                >
                  <i class="ri-check-double-fill fw-bold fs-5"></i>
                </button>

                <button
                  class="btn btn-rounded btn-floating text-danger d-flex align-items-center justify-content-center"
                  @click="deleteTask(task.id)"
                >
                  <i class="ri-delete-bin-2-line fw-bold fs-5"></i>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
        <tbody v-else>
          <td colspan="5" class="bg-white">
            <NoData class="mx-auto" message="No tasks found" />
          </td>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped></style>
