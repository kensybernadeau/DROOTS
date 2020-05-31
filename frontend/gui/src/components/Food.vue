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
              :items="FoodObjectsList"
              :search="search"
              class="elevation-1"
              max-heigth="500px"
            >
              <template v-slot:top>
                <v-toolbar flat color="white">
                  <v-toolbar-title>Food</v-toolbar-title>
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
                      <v-btn color="#39b54a" dark class="mb-2" v-on="on">Add Food</v-btn>
                    </template>
                    <v-card >
                      <v-card-title>
                        <span class="headline">{{ formTitle }}</span>
                      </v-card-title>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="6">
                              <v-text-field v-model="editedFoodObject.food_name"
                              label="Name"
                              :counter="10"
                              :rules="[ v => !!v || 'user name is required', v => (v && v.length <= 10) || 'Name must be less than 10 characters' ]"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="6">
                              <v-text-field v-model="editedFoodObject.food_exp_date"
                              label="Expiration Date"
                              :counter="10"
                              :rules="[ v => !!v || 'user first name is required', v => (v && v.length <= 10) || 'Name must be less than 10 characters' ]"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="6">
                              <v-select
                                v-model="editedFoodObject.food_type"
                              :rules="[ v => !!v || 'user last name is required']"
                                :items="['Dry','Baby Food', 'Canned']"
                                label="Type"
                                flat >
                            </v-select>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field v-model="editedFoodObject.food_description"
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
      { text: 'Food Id', align: 'start', sortable: true, value: 'food_id' },
      { text: 'Resource Id', align: 'start', sortable: false, value: 'resource_id' },
      { text: 'Name', align: 'start', sortable: false, value: 'food_name' },
      { text: 'Type', align: 'start', sortable: false, value: 'food_type' },
      { text: 'Exp Date', align: 'start', sortable: false, value: 'food_exp_date' },
      { text: 'Description', align: 'start', sortable: false, value: 'food_description' },
    //   { text: 'Actions', value: 'actions', sortable: false }
    ],
    FoodObjectsList: [],
    editedFoodObjectIndex: -1,
    editedFoodObject: {
      food_name: '',
      food_exp_date: '',
      food_type: '',
      food_description: '',
      food_date: this.date
    },
    defaultFoodObject: {
      food_name: '',
      food_exp_date: '',
      food_type: '',
      food_description: '',
      food_date: this.date
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
      return this.editedFoodObjectIndex === -1 ? 'New Food' : 'Edit Tag'
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
        'http://localhost:5000/droots/resources/food'
        )
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data.Food)
          this.FoodObjectsList = data.Food
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
      this.editedFoodObjectIndex = this.FoodObjectsList.indexOf(item)
      this.editedFoodObject = Object.assign({}, item)
      this.dialog = true
    },
    /**
     *
     */
    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedFoodObject = Object.assign({}, this.defaultFoodObject)
        this.editedFoodObjectIndex = -1
      })
    },
    /**
     *
     */
    save: async function () {
      if (this.editedFoodObjectIndex > -1) {
        // the existing tag was edited
        // this.editedFoodObject.tname = this.editedFoodObject.tname.toUpperCase()
        // Object.assign(this.FoodObjectsList[this.editedFoodObjectIndex], this.editedFoodObject)
        // await fetch(
        //   process.env.VUE_APP_API_HOST + process.env.VUE_APP_EDIT_TAG_1 + this.editedFoodObject.tid + process.env.VUE_APP_EDIT_TAG_2,
        //   {
        //     method: 'POST',
        //     mode: 'cors',
        //     credential: 'include',
        //     headers: {
        //       'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ tname: this.editedFoodObject.tname })
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
        // this.defaultFoodObject.tname = this.defaultFoodObject.tname
        await fetch(
          'http://localhost:5000/droots/resources/food',
          {
            method: 'POST',
            mode: 'cors',
            credential: 'include',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.editedFoodObject)
          })
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok')
            }
            return response.json()
          })
          .then(data => {
            // this.editedFoodObject.tid = data.tid // update to new websites urls
            this.FoodObjectsList.push(data.Food)
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