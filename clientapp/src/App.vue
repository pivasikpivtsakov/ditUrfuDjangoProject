<template>
  <div id="app">
    <div class="center-container">
      <button class="action-button main-action" v-on:click="selectDir">Выбрать направление обучения</button>
    </div>
    <modal-page v-show="isModalVisible" v-on:close="hideModalPage"
                header-text="Руководители направлений получат уведомление о новой заявке. Вы можете выбрать одно направление или несколько.">
      <dir-group-view>
        <accordion v-for="dg in dirGroups" v-bind:key="dg.code"
                   v-bind:button-text="parentAccordionText(dg)"
                   v-bind:expandable="true"
                   v-model="dg.selected"
                   v-on:change="selectDirGroup(dg)">
          <accordion v-for="d in dg.directions" v-bind:key="d.code"
                     v-bind:button-text="childAccordionText(dg, d)"
                     v-model="d.selected"
                     v-on:change="updateDirGroup(dg)"/>
        </accordion>

        <div class="buttons">
          <span class="sending">{{isSending}}</span>
          <button class="action-button" v-on:click="hideModalPage">Отмена</button>
          <button class="action-button main-action" v-on:click="applyToServer">Применить</button>
        </div>
      </dir-group-view>
    </modal-page>
  </div>
</template>

<script>
import ModalPage from "@/components/ModalPage";
import DirGroupView from "@/components/DirGroupView";
import Accordion from "@/components/Accordion";
import {DirGroup} from "@/api/dirgroup.js";
import {SendingState} from "@/api/sendingState";

export default {
  name: 'App',
  components: {
    Accordion,
    DirGroupView,
    ModalPage

  },
  data() {
    return {
      isModalVisible: false,
      dirGroups: [],
      isSending: SendingState.NOTHING,
    }
  },
  methods: {
    async selectDir() {
      this.isModalVisible = true
      let dirGroupsFetched = await DirGroup.list()
      for (let dg of dirGroupsFetched) {
        dg.selected = DirGroup.getSelected(dg)
      }
      this.dirGroups = dirGroupsFetched
    },
    hideModalPage() {
      this.isSending = SendingState.NOTHING
      this.isModalVisible = false
    },
    async applyToServer() {
      this.isSending = SendingState.SENDING
      let tickedDirections = []
      for (let dg of this.dirGroups) {
        for (const d of dg.directions) {
          if (d.selected) {
            tickedDirections.push(`${dg.code}.${d.code}`)
          }
        }
      }
      const response = DirGroup.applySelected(tickedDirections)
      if ((await response).status === 200) {
        this.isSending = SendingState.SENT
      } else {
        this.isSending = SendingState.UNSENT
      }
    },
    parentAccordionText(dg) {
      return `${dg.code.toString()} ${dg.name}`
    },
    childAccordionText(dg, d) {
      return `${dg.code.toString()}.${d.code.toString()} ${d.name}`
    },
    selectDirGroup(dg) {
      DirGroup.selectGroup(dg)
    },
    updateDirGroup(dg) {
      DirGroup.selectDir(dg)
    }
  },
}
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.center-container {
  display: flex;
  align-content: center;
  align-items: center;
  justify-content: center;
  height: 100vh;

}

.buttons {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
  flex-wrap: wrap;
  align-items: baseline;
}

.action-button {
  background-color: #6E757C;
  margin: 5px;
  border: none;
  border-radius: 5px;
  height: 30px;
  padding-left: 10px;
  padding-right: 10px;
  color: white;
  transition: box-shadow 0.2s ease-out, filter 0.2s ease-out;
}

.action-button:hover{
  box-shadow: 3px 3px 5px 1px rgba(0, 0, 0, 0.2);
  transition: 0.2s;
}

.action-button:active {
  filter: brightness(0.9);
  transition: 0.2s;
}

.main-action {
  background-color: #327DF6;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}

</style>
