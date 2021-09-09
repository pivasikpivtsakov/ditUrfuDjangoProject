<template>
  <transition name="fade">
  <div class="fill">
    <window v-on:close="windowClosed" v-bind:header-text="headerText">
      <slot></slot>
    </window>
  </div>
  </transition>
</template>

<script>
import Window from "@/components/Window";
export default {
  name: "ModalPage",
  components: {Window},
  props: {
    headerText: String,
  },
  methods:{
    windowClosed () {
      this.$emit('close')
    }
  },
}
</script>

<style scoped>

.fill {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(110, 117, 124, 0.5);
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>