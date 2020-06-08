<template>
    <span>
        <home-hero></home-hero>
    </span>
</template>

<script>
// @ is an alias to /src
import HomeHero from '@/components/HomeHero.vue';

export default {
    name: 'Home',
    components: {
        HomeHero
    }
};
</script>
