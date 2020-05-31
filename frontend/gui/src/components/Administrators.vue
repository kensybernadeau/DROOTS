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
              :items="UserObjectsList"
              :search="search"
              class="elevation-1"
              max-heigth="500px"
            >
              <template v-slot:top>
                <v-toolbar flat color="white">
                  <v-toolbar-title>Users</v-toolbar-title>
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
                      <v-btn color="#39b54a" dark class="mb-2" v-on="on">Add User</v-btn>
                    </template>
                    <v-card >
                      <v-card-title>
                        <span class="headline">{{ formTitle }}</span>
                      </v-card-title>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="6">
                              <v-text-field v-model="editedUserObject.user_uname"
                              label="User Name"
                              :counter="10"
                              :rules="[ v => !!v || 'user name is required', v => (v && v.length <= 10) || 'Name must be less than 10 characters' ]"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="6">
                              <v-text-field v-model="editedUserObject.user_fname"
                              label="First Name"
                              :counter="10"
                              :rules="[ v => !!v || 'user first name is required', v => (v && v.length <= 10) || 'Name must be less than 10 characters' ]"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="6">
                              <v-text-field v-model="editedUserObject.user_lname"
                              label="Last Name"
                              :counter="20"
                              :rules="[ v => !!v || 'user last name is required', v => (v && v.length <= 20) || 'Name must be less than 20 characters' ]"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="6">
                              <v-text-field v-model="editedUserObject.user_passwd"
                              label="password"
                              :counter="10"
                              :rules="[ v => !!v || 'pasword is required', v => (v && v.length <= 10) || 'password must be less than 10 characters' ]"
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
      { text: 'Id', align: 'start', sortable: true, value: 'user_id' },
      { text: 'User Name', align: 'start', sortable: true, value: 'user_uname' },
      { text: 'First Name', align: 'start', sortable: true, value: 'user_fname' },
      { text: 'Last Name', align: 'start', sortable: true, value: 'user_lname' },
      { text: 'Password', align: 'start', sortable: true, value: 'user_passwd' },
    //   { text: 'Actions', value: 'actions', sortable: false }
    ],
    UserObjectsList: [],
    editedUserObjectIndex: -1,
    editedUserObject: {
      user_fname: '',
      user_lname: '',
      user_passwd: null,
      user_uname: ''
    },
    defaultUserObject: {
      user_fname: '',
      user_id: -1,
      user_lname: '',
      user_passwd: '',
      user_uname: ''
    }
    }),
    async mounted () {
    await this.fetchUsers()
    console.log(this.users)
  },
  computed: {
    /**
     *
     */
    formTitle () {
      return this.editedUserObjectIndex === -1 ? 'New User' : 'Edit Tag'
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
    fetchUsers: async function () {
      console.log('fetching')
  await fetch(
        'http://localhost:5000/droots/administrators'
        )
        .then(response => {
          return response.json()
        })
        .then(data => {
          console.log(data)
          this.UserObjectsList = data.Administrators
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
      this.editedUserObjectIndex = this.UserObjectsList.indexOf(item)
      this.editedUserObject = Object.assign({}, item)
      this.dialog = true
    },
    /**
     *
     */
    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedUserObject = Object.assign({}, this.defaultUserObject)
        this.editedUserObjectIndex = -1
      })
    },
    /**
     *
     */
    save: async function () {
      if (this.editedUserObjectIndex > -1) {
        // the existing tag was edited
        // this.editedUserObject.tname = this.editedUserObject.tname.toUpperCase()
        // Object.assign(this.UserObjectsList[this.editedUserObjectIndex], this.editedUserObject)
        // await fetch(
        //   process.env.VUE_APP_API_HOST + process.env.VUE_APP_EDIT_TAG_1 + this.editedUserObject.tid + process.env.VUE_APP_EDIT_TAG_2,
        //   {
        //     method: 'POST',
        //     mode: 'cors',
        //     credential: 'include',
        //     headers: {
        //       'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ tname: this.editedUserObject.tname })
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
        // this.defaultUserObject.tname = this.defaultUserObject.tname
        this.defaultUserObject.user_passwd = parseInt(this.defaultUserObject.user_passwd, 10)
        await fetch(
          'http://localhost:5000/droots/administrators',
          {
            method: 'POST',
            mode: 'cors',
            credential: 'include',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.editedUserObject)
          })
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok')
            }
            return response.json()
          })
        //   .then(data => {
        //     // this.editedUserObject.tid = data.tid // update to new websites urls
        //   })
          .catch((error) => {
            console.error('There has been a problem with your fetch operation:', error)
          })
      }
      this.close()
    }
  }
  }
</script>