<template>
    <span>
        <register-movies></register-movies>
        <get-movies></get-movies>
    </span>
</template>

<script>
// @ is an alias to /src
import RegisterMovies from '@/components/RegisterMovies.vue';
import GetMovies from '@/components/GetMovies.vue';

export default {
    name: 'Home',
    components: {
        RegisterMovies,
        GetMovies
    }
};
</script>
