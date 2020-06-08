<template>
    <v-container style="margin-top: 5%">
        <v-btn class="mr-4" @click="getMovies">Get Movies</v-btn>
        <v-flex d-flex style="margin-top:3%">
            <v-layout wrap>
                <v-flex md4 v-for="item in movies_list" :key="item.id">
                    <v-card class="mx-auto" max-width="344" outlined>
                        <v-list-item three-line>
                            <v-list-item-content>
                                <div class="overline mb-4">Filme</div>
                                <v-list-item-title class="headline mb-1">{{
                                    item.movie_name
                                }}</v-list-item-title>
                                <v-list-item-subtitle>
                                    {{ item.description }}</v-list-item-subtitle
                                >
                            </v-list-item-content>
                        </v-list-item>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-flex>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    name: 'GetMovies',
    data: () => ({
        movies_list: ''
    }),

    computed: {},

    methods: {
        getMovies() {
            var name = this.name;
            var description = this.description;

            console.log(name);
            console.log(description);
            axios({
                method: 'GET',
                url:
                    'https://k77aqaz6we.execute-api.us-east-1.amazonaws.com/prod/get-movies'
            }).then(response => {
                console.log(response.data);
                this.movies_list = response.data;
            });
        }
    }
};
</script>
