<template>
    <v-container>
        <form id="moviesForm">
            <v-text-field
                v-model="name"
                :error-messages="nameErrors"
                label="Name"
                required
                @input="$v.name.$touch()"
                @blur="$v.name.$touch()"
            ></v-text-field>
            <v-text-field
                v-model="description"
                :error-messages="descriptionErrors"
                label="Description"
                required
                @input="$v.description.$touch()"
                @blur="$v.description.$touch()"
            ></v-text-field>

            <v-btn class="mr-4" @click="postPost">submit</v-btn>
            <v-btn @click="clear">clear</v-btn>
        </form>
        {{ output }}
    </v-container>
</template>

<script>
import axios from 'axios';
import { validationMixin } from 'vuelidate';
import { required, maxLength, email } from 'vuelidate/lib/validators';

export default {
    name: 'RegisterMovies',
    mixins: [validationMixin],

    validations: {
        name: { required, maxLength: maxLength(10) },
        email: { required, email },
        select: { required },
        checkbox: {
            checked(val) {
                return val;
            }
        }
    },

    data: () => ({
        name: '',
        description: '',
        output: '',
        show: false
    }),

    computed: {},

    methods: {
        submit() {
            this.$v.$touch();
        },
        clear() {
            this.$v.$reset();
            this.name = '';
            this.description = '';
        },
        postPost() {
            var name = this.name;
            var description = this.description;

            console.log(name);
            console.log(description);
            axios({
                method: 'POST',
                url:
                    'https://k77aqaz6we.execute-api.us-east-1.amazonaws.com/prod/put-movie',
                data: {
                    movie_name: name,
                    description: description
                }
            }).then(response => {
                console.log(response.data);
                this.output = name + ' Cadastrado com sucesso!';
                this.name = '';
                this.description = '';
            });
        }
    }
};
</script>
