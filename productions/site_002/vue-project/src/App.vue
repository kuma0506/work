<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">PEEK</router-link>｜
      <router-link to="/">DESIGN</router-link>｜
      <router-link to="/">STORY</router-link>｜
      <router-link to="/">TUTORIAL</router-link>｜
      <router-link to="/">FAQ</router-link>｜
      <router-link to="/">PRESS KIT</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
