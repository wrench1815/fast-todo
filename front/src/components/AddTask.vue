<script setup lang="ts">
import { onMounted, ref, inject } from 'vue';
import * as mdb from 'mdb-ui-kit';
import type { AxiosStatic } from 'axios';

const axios = inject('axios') as AxiosStatic;

const task = ref({
  task: '',
});

const emit = defineEmits(['task-add']);

async function addTask() {
  return axios
    .post('todo/', task.value)
    .then((res) => {
      if (res.status == 201) {
        emit('task-add');
        document.getElementById('AddTaskClose')?.click();
      }
    })
    .catch((err) => {
      console.log(err);
      console.log(err.response);
      console.log(err.response.data);
    });
}

function modalClose() {
  const form = document.querySelector('#addTaskForm') as HTMLFormElement;
  task.value.task = '';
  form.reset();
}

onMounted(() => {
  // initialize form elements
  document.querySelectorAll('.form-outline').forEach((formOutline) => {
    new mdb.Input(formOutline).init();
  });
});
</script>

<template>
  <!-- Modal -->
  <div
    class="modal top fade"
    id="AddTask"
    tabindex="-1"
    aria-labelledby="AddTaskLabel"
    aria-hidden="true"
    data-mdb-backdrop="static"
    data-mdb-keyboard="false"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="AddTaskLabel">Add a new Task</h5>
          <button
            id="AddTaskClose"
            type="button"
            class="btn-close"
            data-mdb-dismiss="modal"
            aria-label="Close"
            @click="modalClose"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addTask" id="addTaskForm">
            <!-- Task -->
            <div class="form-outline mb-4">
              <textarea
                rows="4"
                class="form-control"
                v-model="task.task"
              ></textarea>
              <label class="form-label">
                Task <span class="text-danger">*</span>
              </label>
            </div>

            <!-- Submit button -->
            <button type="submit" class="btn btn-primary btn-block">
              Add Task
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
