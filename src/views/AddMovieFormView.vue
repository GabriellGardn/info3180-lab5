<template>
  <div>
    <h1>Create a new movie</h1>
    <MovieForm />
  </div>
</template>

<script>
import MovieForm from "@/components/MovieForm.vue";

export default {
  components: {
    MovieForm,
  },
};
</script>
