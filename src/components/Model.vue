<template>
  <v-card>
    <div class="loading" v-if="loading">
      ...loading
    </div>
    <div class="error" v-if="error">
      {{ error }}
    </div>
    <div class="content" v-if="content">
      <p>The card of: {{ $route.params.model }}</p>
      <v-data-table
        v-model="selected"
        :headers="headers"
        :items="rows"
        :pagination.sync="pagination"
        select-all
        item-key="id"
        class="elevation-1"
      >
        <template v-slot:headers="props">
          <tr>
            <th
              v-for="header in props.headers"
              v-show="header.value != 'id'"
              :key="header.text"
              :class="[
                'column sortable',
                pagination.descending ? 'desc' : 'asc',
                header.value === pagination.sortBy ? 'active' : ''
              ]"
              @click="changeSort(header.value)"
            >
              <v-icon small>arrow_upward</v-icon>
              {{ header.text }}
            </th>
          </tr>
        </template>
        <template v-slot:items="props">
          <tr
            :active="props.selected"
            @click="props.selected = !props.selected"
          >
            <td
              v-for="header in props.item.headers"
              v-show="header.value != 'id'"
              :key="header.text"
            >
              {{ props.item.data[header.value] }}
            </td>
          </tr>
        </template>
      </v-data-table>
      <v-btn
        v-if="$route.params.form"
        round
        outline
        @click.native.prevent="showForm()"
        >Dodaj</v-btn
      >
    </div>
  </v-card>
</template>

<script>
import $backend from "../backend";

export default {
  data() {
    return {
      loading: false,
      content: false,
      error: null,
      rows: [],
      headers: [],
      pagination: {
        sortBy: "name"
      },
      selected: []
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    //fetch on route change
    $route: "fetchData"
  },
  methods: {
    fetchData() {
      this.error = this.content = null;
      this.loading = true;
      $backend
        .getModel(this.$route.params.model)
        .then(responseData => {
          this.loading = false;
          this.content = true;
          this.headers = responseData.headers.map(item => {
            return { text: item.toUpperCase(), value: item };
          });
          this.rows = responseData.content.map(row => {
            return { headers: this.headers, data: row, id: row.id };
          });
        })
        .catch(error => {
          this.error = error.message;
        });
    },
    changeSort(column) {
      if (this.pagination.sortBy === column) {
        this.pagination.descending = !this.pagination.descending;
      } else {
        this.pagination.sortBy = column;
        this.pagination.descending = false;
      }
    },
    showForm: function() {
      this.$emit("show-form", this.$route.params.form);
    }
  }
};
</script>
