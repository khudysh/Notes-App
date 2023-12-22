<template>
  <div class="home">
    <div class="filters">
      <select v-model="sortSelected" @change="sort">
        <option v-for="option in sortOptions"  v-bind:value="option.value">
          {{ option.text }}
        </option>
      </select>
    </div>
    <div class="cards">
      <template v-for="note in notes">
        <div class="card" @click="chooseNote(note)">
          <button class="closeNote" v-if="formData.id == note.id" @click.stop="unchooseNote">X</button>
          <h1 class="title">{{ note.title }}</h1>
          <p class="text">{{ note.text }}</p>
          <sub class="date">{{ note.created }}</sub>
        </div>
      </template>
    </div>
    <div class="form">
      <input v-model="formData.title" type="text" class="title_form">
      <textarea v-model="formData.text" cols="30" rows="10" class="text_form"></textarea>
      <button @click="saveNote" v-if="formData.id != ''">Сохранить</button>
      <button @click="addNote" v-else>Создать</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  data() {
    return {
      formData: {
        id: '',
        title: '',
        text: '',
        created: '',
      },
      sortSelected: '',
      sortOptions: [
        { text: 'От старых к новым', value: 'toNew' },
        { text: 'От новых к старым', value: 'toOld' },
      ]
    }
  },
  methods: {
    async sort() {
      console.log('sort')
      await this.$store.dispatch('fetchAllNotes', this.sortSelected)
    },
    unchooseNote() {
      this.formData.title = ''
      this.formData.text = ''
      this.formData.id = ''
      this.formData.created = ''
    },
    chooseNote(note: any) {
      this.formData.title = note.title
      this.formData.text = note.text
      this.formData.id = note.id
      this.formData.created = note.created
    },
    saveNote() {
      if (this.formData.id == '') return

      this.$store.dispatch('updateNote', this.formData)
    },
    addNote() {
      // this.formData.created = Date.UTC
      this.$store.dispatch('createNote', this.formData)
    }
  },
  async mounted() {
    await this.$store.dispatch('fetchAllNotes')
  },
  computed: {
    notes() {
      return this.$store.state.noteState.notes
    }
  }
});
</script>

<style scoped>
.form {
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: auto;
}

.cards {
  display: flex;
  flex-wrap: wrap;
}

.card {
  margin: 10px;
  width: 175px;
  height: max-content;
  background-color: rgb(255, 226, 153);
  padding: 10px;
  position: relative;
}

.closeNote {
  position: absolute;
  top: -10px;
  right: -10px;
}

.card * {
  cursor: default
}

.text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>