<template>
  <v-app>
    <v-app-bar color="#FFCC80" app height="60">
      <v-app-bar-nav-icon
        @click="showDrawer = !showDrawer"
      ></v-app-bar-nav-icon>
      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer v-model="showDrawer" absolute bottom temporary>
      <v-list nav dense>
        <v-list-item-group>
          <v-list-item v-for="(drawerMenu, idx) in drawerMenus" :key="idx">
            <v-list-item-title>{{ drawerMenu.Menu }}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <nuxt class="nuxt" />
  </v-app>
</template>

<script lang="ts">
import { Vue, Component } from "nuxt-property-decorator";

@Component
export default class Default extends Vue {
  showDrawer = false;

  drawerMenus = [
    { Menu: "Menu1" },
    { Menu: "Menu2" },
    { Menu: "Menu3" },
    { Menu: "Menu4" },
    { Menu: "Menu5" },
    { Menu: "Menu6" },
  ];
}
</script>
<style scoped>
.nuxt {
  margin: auto;
  margin-top: 7rem;
}
</style>