<template>
<v-container class="grey lighten-5 mb-6" style="max-width: 600px;">
      <v-text-field
            v-model="search"
            label="Search"
            class="mb-5"
            prepend-inner-icon="mdi-magnify"
            flat
            single-line
            hide-details
          ></v-text-field>
    <v-card class="justify-center" >
        <v-card >
            <v-data-table
              :headers="headers"
              :items="ObjectsList"
              :search="search"
              class="elevation-1"
              max-heigth="500px"
            >
              <template v-slot:top>
                <v-toolbar flat color="white">
                  <v-toolbar-title>Ice</v-toolbar-title>
                  <v-divider
                    class="mx-4"
                    inset
                    vertical
                  ></v-divider>
                  <v-spacer></v-spacer>
                  <v-form
                    ref="form"
                    v-model="valid"
                    class="ma-6"
                  >
                  <v-dialog persistent v-model="dialog" max-width="400px">
                    <template v-slot:activator="{ on }">
                      <v-btn color="#39b54a" dark class="mb-2" v-on="on">Add Ice</v-btn>
                    </template>
                    <v-card >
                      <v-card-title>
                        <span class="headline">{{ formTitle }}</span>
                      </v-card-title>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="6">
                              <v-text-field v-model="editedObject.ice_name"
                              label="Name"
                              :counter="10"
                              :rules="[ v => !!v || 'user name is required', v => (v && v.length <= 10) || 'Name must be less than 10 characters' ]"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field v-model="editedObject.ice_description"
                              label="Description"
                              :counter="250"
                              :rules="[ v => !!v || 'description is required', v => (v && v.length <= 250) || 'description must be less than 250 characters' ]"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="#ff3e4c" text @click="close">Cancel</v-btn>
                        <v-btn color="#24324f" text :disabled="!valid"  @click="save">Save</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  </v-form>
                </v-toolbar>
              </template>
              <template v-slot:item.actions="{ item }">
                <v-icon
                  small
                  class="mr-2"
                  @click="editTagObject(item)"
                >
                  mdi-pencil
                </v-icon>
              </template>
            </v-data-table>
        </v-card>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',
    props: {
      source: String,
    },
    data: () => ({
    search: '',
    valid: false,
    dialog: false,
      headers: [
      { text: 'Ice Id', align: 'start', sortable: true, value: 'ice_id' },
      { text: 'Resource Id', align: 'start', sortable: false, value: 'resource_id' },
      { text: 'Name', align: 'start', sortable: false, value: 'ice_name' },
      { text: 'Description', align: 'start', sortable: false, value: 'ice_description' },
    //   { text: 'Actions', value: 'actions', sortable: false }
    ],
    ObjectsList: [],
    editedObjectIndex: -1,
    editedObject: {
      ice_name: '',
      ice_description: '',
      ice_date: null
    },
    defaultObject: {
       ice_name: '',
      ice_description: '',
      ice_date: null
    }
    }),
    async mounted () {
    await this.fetchFood()
  },
  computed: {
    /**
     *
     */
    formTitle () {
      return this.editedObjectIndex === -1 ? 'New Ice' : 'Edit Tag'
    },
    date () {
        var today = new Date()
        var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate()
        return date
    }
  },
  watch: {
    /**
     *
     */
    dialog (val) {
      val || this.close()
    }
  },
  methods: {
    fetchFood: async function () {
      console.log('fetching')
  await fetch(
        'http://localhost:5000/droots/resources/ice'
        )
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data.Food)
          this.ObjectsList = data.Ice
        })
        return
    },
    validate: function () {
      this.$refs.form.validate()
      // if (this.valid) {
      //   this.save()
      // }
    },
     /**
     *
     */
    editTagObject (item) {
      this.editedObjectIndex = this.ObjectsList.indexOf(item)
      this.editedObject = Object.assign({}, item)
      this.dialog = true
    },
    /**
     *
     */
    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedObject = Object.assign({}, this.defaultObject)
        this.editedObjectIndex = -1
      })
    },
    /**
     *
     */
    save: async function () {
      if (this.editedObjectIndex > -1) {
        // the existing tag was edited
        // this.editedObject.tname = this.editedObject.tname.toUpperCase()
        // Object.assign(this.ObjectsList[this.editedObjectIndex], this.editedObject)
        // await fetch(
        //   process.env.VUE_APP_API_HOST + process.env.VUE_APP_EDIT_TAG_1 + this.editedObject.tid + process.env.VUE_APP_EDIT_TAG_2,
        //   {
        //     method: 'POST',
        //     mode: 'cors',
        //     credential: 'include',
        //     headers: {
        //       'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ tname: this.editedObject.tname })
        //   })
        //   .then(response => {
        //     if (!response.ok) {
        //       throw new Error('Network response was not ok')
        //     }
        //     return response.json()
        //   })
        //   .catch((error) => {
        //     console.error('There has been a problem with your fetch operation:', error)
        //   })
      } else {
        // a new tag was created
        // this.defaultObject.tname = this.defaultObject.tname
        this.editedObject.ice_date = this.date
        await fetch(
          'http://localhost:5000/droots/resources/ice',
          {
            method: 'POST',
            mode: 'cors',
            credential: 'include',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.editedObject)
          })
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok')
            }
            return response.json()
          })
          .then(data => {
            // this.editedObject.tid = data.tid // update to new websites urls
            this.ObjectsList.push(data.Ice)
          })
          .catch((error) => {
            console.error('There has been a problem with your fetch operation:', error)
          })
      }
      this.close()
    }
  }
  }
</script>