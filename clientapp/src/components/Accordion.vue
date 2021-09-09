<template>
  <div class="accordion-template">
    <div class="accordion" v-on:click="accordionClick">
      <input type="checkbox" class="accordion-checkbox" v-bind:checked="checked" v-on:change="$emit('change', $event.target.checked)" v-on:click="accordionClick"/>
      <span class="accordion-text">{{ buttonText }}</span>
    </div>
    <div class="panel" ref="panel">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "Accordion",
  model: {
    prop: 'checked',
    event: 'change',
  },
  props: {
    buttonText: String,
    expandable: Boolean,
    checked: Boolean,
  },
  methods: {
    accordionClick () {
      if (this.expandable) {
        const panel = this.$refs.panel
        panel.style.maxHeight = panel.style.maxHeight ? null : panel.scrollHeight + 'px'
      }
    }
  }
}
</script>

<style scoped>
.accordion {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  color: #444;
  cursor: pointer;
  width: 100%;
  text-align: left;
  transition: 0.2s;
  padding: 10px;
  box-sizing: border-box;
  box-shadow: 0 0 3px 1px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
  margin-bottom: 3px;
  margin-top: 3px;
}

.accordion-text {
  flex: 1 1 auto;
  word-break: normal;
}

.active, .accordion:hover {
  background-color: #ccc;
}

.panel {
  padding: 0 18px;
  background-color: white;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
}

.accordion-checkbox {
  height: 20px;
  width: 20px;
  flex: 0 1 20px;
}
</style>