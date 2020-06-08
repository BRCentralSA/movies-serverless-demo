<template>
    <v-card color="grey lighten-4" flat height="100px" tile>
        <v-toolbar dense>
            <v-app-bar-nav-icon></v-app-bar-nav-icon>

            <v-toolbar-title>Movies App</v-toolbar-title>
            <router-link to="/" style="margin-left: 2%">
                <v-btn flat class="hidden-sm-and-down">Home</v-btn>
            </router-link>
            <router-link to="/register_movies" style="margin-left: 2%">
                <v-btn flat class="hidden-sm-and-down">Movies</v-btn>
            </router-link>
        </v-toolbar>
    </v-card>
</template>

<script>
export default {
    name: 'AppNavigation'
};
</script>

<style scoped></style>
