<template>
  <v-card width="400" height="330" class="text-center">
    <v-card-title class="mb-8 orange lighten-4 justify-center"
      >User Login</v-card-title
    >
    <v-text-field class="mx-8" label="userId" outlined dense></v-text-field>
    <v-text-field class="mx-8" label="password" outlined dense></v-text-field>
    <v-btn class="orange mt-9 lighten-4" @click="login"> Login</v-btn>
  </v-card>
</template>

<script lang="ts">
import { Vue, Component } from "nuxt-property-decorator";

@Component
export default class Index extends Vue {
  login() {
    this.$router.push("/beautySalonList");
  }
}
</script>
