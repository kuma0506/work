<template>
  <v-card class="overflow-hidden card_1">
    <v-app-bar
      color="blue-grey"
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
    >
      <a href="/"><img src="../assets/images/logo.svg" alt="logo"></a>
      <v-spacer></v-spacer>
      <v-app-bar-nav-icon @click="drawer = true" class="white--text"></v-app-bar-nav-icon>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      right
      temporary
    > <!-- temporary はドロワー非表示制御-->
      <v-list
        nav
        dense
      >
        <v-list-item-group color="blue-grey">
          <v-list-item>
            <v-list-item-title><a href="/about" class="grey--text">ABOUT</a></v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title><a href="/main" class="grey--text">MAIN</a></v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title><a href="/insert" class="grey--text">INSERT</a></v-list-item-title>
          </v-list-item>                    
          <v-list-item>
            <v-list-item-title><a href="/contact" class="grey--text">CONTACT</a></v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-sheet
      id="scrolling-techniques-7"
      class="overflow-y-auto"
      max-height="100vh"
    >
    </v-sheet>
  </v-card>
</template>

<style lang="scss" scoped>
.card_1 {
  position: fixed;
  width: 100%;
  z-index:100; /* 数値が大きいものが前面 */
}
.header-1 {
  height: 7vh;
  background-color: #DCDCDC;
}
img {
  margin: 1vh auto;
  height: 5vh;
  fill: white;
}
a {
  text-decoration: none;
  display: block;
}
</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component({
  components: {
  },
})
export default class HeaderCom extends Vue {
  data() {
    return {
      drawer: false
    }
  }
}
</script>