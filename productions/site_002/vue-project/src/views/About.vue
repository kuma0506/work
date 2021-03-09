<template>
  <v-app>
    <HeaderCom/>
    <div id="div_1">
      <h2>Welcome to this site</h2>
      <h2>Here we will help you shape your memories.</h2>
      <img src="../assets/images/image_3.jpg" class="img_1" alt="image_3">
      <h2>I have many memories so far.</h2>
      <h2>Do you remember everything?</h2>
      <h2>I think it's difficult.</h2>
      <h2>This app solves such troubles and leaves</h2>
      <h2>all memories as a form.</h2>
      <img src="../assets/images/image_4.jpg" class="img_1" alt="image_4">
      <h2>Let's get started</h2>
    </div>
    <div id="div_2">
      <FooterCom/>
    </div>
  </v-app>
</template>
<style lang="scss" scoped>
#div_1 {
  margin-top: 15vh;
  text-align: center;
  color: grey;
  
}
#div_2 {
  margin-top: 11vh;
}
.img_1 {
  margin: 3vh auto;
  width: 50%;
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
export default class About extends Vue {
  data(){
    return {
    }
  }
}
</script>