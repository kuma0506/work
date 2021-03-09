<template>
  <v-footer 
    padless 
    class="footer white--text"
    color="blue-grey"
    >
    <v-col
      class="text-center"
      cols="12"
    >
      @{{ new Date().getFullYear() }} — <strong>Vuetify</strong>
    </v-col>
  </v-footer>
</template>

<style lang="scss" scoped>

</style>

<style lang="scss" scoped>
@import '../assets/ress/ress.min.css';
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    font-size: 0.5rem;

}
</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component({
  components: {
  },
})
export default class FooterCom extends Vue {
  data() {
    return {
    }
  }
}
</script>