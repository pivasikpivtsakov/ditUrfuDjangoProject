<template>
  <div class="window-container">
    <div class="window-header">
      <span class="header-text">{{ headerText }}</span>
      <span class="close-button" v-on:click="closeButtonClick">&times;</span>
    </div>
    <div class="window-content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "Window",
  props: {
    headerText: String,
  },
  methods: {
    closeButtonClick() {
      this.$emit('close')
    }
  },
}
</script>

<style scoped>
.window-container {
  background-color: #fefefe;
  margin-right: auto;
  margin-left: auto;
  margin-top: 100px;
  padding: 20px;
  width: 80%;
  border-radius: 10px;
  box-shadow: 0 0 20px 10px rgba(0, 0, 0, 0.2);
}

.window-header {
  display: flex;
  align-items: center;
}

.window-content {
  margin-top: 20px;
}

.close-button {
  font-size: 28px;
  flex: 0 1 28px;
}

.close-button:hover,
.close-button:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}

.header-text {
  flex: 1 1 auto;
  word-break: normal;
  text-align: left;
}

</style>