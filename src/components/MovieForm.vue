<script setup>
import { onMounted, ref } from "vue";

let csrf_token = ref("");
let successMessage = ref("");
let errorMessages = ref([]);

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => {
      console.log(error);
    });
}

function saveMovie() {
  let movieForm = document.getElementById("movieForm");
  let form_data = new FormData(movieForm);

  successMessage.value = "";
  errorMessages.value = [];

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value
    }
  })
    .then((response) =>
      response.json().then((data) => ({
        ok: response.ok,
        data
      }))
    )
    .then((data) => {
      if (data.ok) {
        successMessage.value = data.data.message;
        errorMessages.value = [];
        movieForm.reset();
        getCsrfToken();
        return;
      }

      successMessage.value = "";
      errorMessages.value = data.data.errors || ["Something went wrong."];
    })
    .catch((error) => {
      successMessage.value = "";
      errorMessages.value = ["Unable to save movie right now."];
      console.log(error);
    });
}

onMounted(() => {
  getCsrfToken();
});
</script>

<template>
  <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
    <div v-if="successMessage" class="alert alert-success mb-3">
      {{ successMessage }}
    </div>

    <div v-if="errorMessages.length" class="alert alert-danger mb-3">
      <ul class="mb-0">
        <li v-for="error in errorMessages" :key="error">{{ error }}</li>
      </ul>
    </div>

    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input id="title" type="text" name="title" class="form-control" />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea id="description" name="description" class="form-control" rows="4"></textarea>
    </div>

    <div class="form-group mb-4">
      <label for="poster" class="form-label">Poster</label>
      <input id="poster" type="file" name="poster" class="form-control" accept=".jpg,.jpeg,.png" />
    </div>

    <button type="submit" class="btn btn-primary">Save Movie</button>
  </form>
</template>

<style scoped>
.form-control {
  max-width: 100%;
}
</style>
