<template>
  <v-app>
    <div id="div_1">
      <HeaderCom/>
    </div>
    <v-card width="550px" class="mx-auto mt-5">
      <v-card-title>
        <h1 class="display-1 h1_1">Insert</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-file-input show-size prepend-icon="mdi-camera" label="File input"></v-file-input>
          <v-combobox
            show-size
            v-model="select"
            :items="items"
            label="Check"
            multiple
            chips
            prepend-icon="mdi-check"
          ></v-combobox>
          <v-text-field prepend-icon="mdi-key" label="Keyword" />
          <v-card-actions>
            <v-btn 
              class="white--text"
              color="blue-grey"
              to ="/main"
            >
              Insert
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
export default class Insert extends Vue {
  data(){
    return {
        items: ['Menu1','Menu2','Menu3','Menu4','Menu5','Menu6','Menu7','Menu8','Menu9']
    }
  }
}
</script>