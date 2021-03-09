<template>
  <v-app>
    <HeaderCom/>
    <div id="div_1">
    </div>
    <v-card class="mx-auto mt-5 card-1">
      <v-card-title>
        <h1 class="display-1 h1_1 mb-6">Contact</h1>
        <h5 class="headline h1_1" >If you have any inquiries about the site,</h5>
        <h5 class="headline h1_1" >work requests, etc., please contact us</h5>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field prepend-icon="mdi-account-circle" label="UserName" />
          <v-text-field prepend-icon="mdi-email-outline" label="Email-Address" />
        <v-textarea
          prepend-icon="mdi-border-color"
          autocomplete="detail"
          label="Detail"
          placeholder="Please enter details"
        ></v-textarea>
          <v-card-actions>
            <v-btn
              class="white--text"
              color="blue-grey"
              to="/main"
            >
              send
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
  margin-top: 8vh;
}
.card-1 {
  width: 550px;
  
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
export default class Contact extends Vue {
  data(){
    return {
    }
  }
}
</script>