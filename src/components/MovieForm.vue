<template>
  <form @submit.prevent="saveMovie">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" v-model="movie.title" class="form-control" />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Movie Description</label>
      <textarea name="description" v-model="movie.description" class="form-control"></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input type="file" name="poster" @change="onPosterChange" class="form-control" />
    </div>
    <button type="submit" class="btn btn-primary">Save Movie</button>
  </form>
</template>



<script setup>
import { ref } from 'vue';

const title = ref('');
const description = ref('');
const poster = ref(null);
const errors = ref([]);

function saveMovie() {
  errors.value = [];
  
  const formData = new FormData();
  formData.append('title', title.value);
  formData.append('description', description.value);
  formData.append('poster', poster.value);

  fetch('/api/v1/movies', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // display a success message
    })
    .catch(error => {
      console.log(error);
      errors.value = error;
    });
}
</script>
