<script setup>
import { onMounted, ref } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then((response) => response.json())
    .then((data) => {
      movies.value = data.movies || [];
    })
    .catch((error) => {
      console.log(error);
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<template>
  <div class="container">
    <h2 class="mb-4">Movies</h2>

    <div class="row g-4">
      <div v-for="movie in movies" :key="movie.id" class="col-12 col-lg-6">
        <div class="card h-100">
          <div class="row g-0 h-100">
            <div class="col-4">
              <img :src="movie.poster" :alt="movie.title" class="img-fluid rounded-start poster-image" />
            </div>
            <div class="col-8">
              <div class="card-body">
                <h4 class="card-title">{{ movie.title }}</h4>
                <p class="card-text">{{ movie.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.poster-image {
  height: 100%;
  width: 100%;
  object-fit: cover;
}
</style>
