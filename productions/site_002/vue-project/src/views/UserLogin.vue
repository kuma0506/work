<template>
  <v-app>
    <div id="div_1">
      <HeaderCom/>
    </div>
    <v-card class="mx-auto mt-5 card-1">
      <v-card-title>
        <h1 class="display-1 h1_1">Login</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field prepend-icon="mdi-account-circle" label="UserID" />
          <v-text-field 
            v-bind:type="showPassword ? 'text' : 'password'" 
            prepend-icon="mdi-lock" 
            v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" 
            label="Password" 
            @click:append="showPassword = !showPassword" 
          />
          <v-card-actions>
            <v-btn
              class="white--text"
              color="blue-grey"
              to="/main"
            >
              Login
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
    <FooterCom/>
    </v-app>
</template>
<style lang="scss" scoped>
  #div_1 {
    margin-bottom: 8vh;
  }
  .card-1 {
    width: 400px;
    
  }
  .h1_1 {
    color: rgb(116, 116, 116);
  }
</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HeaderCom from '@/components/HeaderCom.vue';
import FooterCom from '@/components/FooterCom.vue';

@Component({
  components: {
    HeaderCom,
    FooterCom
  },
})
export default class UserLogin extends Vue {
}
</script>