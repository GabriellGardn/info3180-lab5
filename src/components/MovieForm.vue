<template>

  <div>
    <form @submit.prevent="saveMovie" id="movieForm">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" v-model="title" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Movie Poster</label>
        <input type="file" name="poster" ref="poster" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Movie Description</label>
        <textarea name="description" v-model="description" class="form-control"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>

</template>



<script setup>

import { ref, onMounted } from 'vue';

let csrf_token = ref("");

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);

      csrf_token.value = data.csrf_token;
    });
}

const title = ref('');
const description = ref('');
const poster = ref(null);
const errors = ref([]);

function saveMovie() {

  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  fetch('/api/v1/movies', {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
  },
  })
    .then(function (response) {
      if (response.ok) {
        console.log("Movie saved successfully!");
      } else {
        console.log("Error saving movie");
      }
  })
    .catch(function (error) {
      console.log(error);
 });
}

onMounted(() => {
  getCsrfToken();
});

</script>


