<script setup lang="ts">
const props = withDefaults(defineProps<{ message: string }>(), {
  message: 'Nothing to see here',
});
</script>

<template>
  <div class="d-flex flex-column align-items-center">
    <!-- Error Background -->
    <div class="position-relative">
      <!-- Error Image -->
      <img
        class="img-fluid"
        src="@/assets/no_data.svg"
        alt="Nothing to see here"
      />

      <!-- Error Message -->
      <div class="text-center position-absolute top error-pos">
        <h4 class="text-primary d-inline-block">
          {{ message }}
        </h4>
      </div>
    </div>
    <!-- Error Background -->
  </div>
</template>

<style scoped>
.error-pos {
  left: 40%;
  right: 6%;
}

.top {
  top: 55%;
}
</style>
