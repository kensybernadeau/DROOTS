<template>
    <v-container class="pb-0">
        <v-app-bar
          :clipped-left="$vuetify.breakpoint.lgAndUp"
          app
          color="#00251a"
          dark
        >
          <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
          <v-toolbar-title
            class="ml-0 pl-4"
          >
            <span class="hidden-sm-and-down" style="color:#afbec8;"><h1>DROOTS</h1></span>
          </v-toolbar-title>
            <v-col class="pt-8" cols="6">
              <v-form
                    ref="searchForm"
                    persistent
                    v-model="validSearch"
                    class="ma-0 pa-0"
                  >
            <v-text-field
            @keydown.enter="followRoute"
            v-model="search"
            v-click-outside="clearValdation"
              flat
              dense
              :rules="[v => /^[a-zA-Z0-9]*$/.test() || 'only serach by keyword, without spaces']"
              solo-inverted
              prepend-inner-icon="mdi-magnify"
              label="Search"
            />
              </v-form>
            </v-col>
            <v-col cols="2" class="pa-0 pt-8 pb-3">
                <v-select
                    v-model="selectedSearch"
                      :items="['resource','request']"
                      label="Type"
                      dense
                      flat
                      solo-inverted >
                </v-select>
            </v-col>
            <v-spacer />
        </v-app-bar>
        <v-navigation-drawer
          v-model="drawer"
          :width="310"
          :clipped="$vuetify.breakpoint.lgAndUp"
          app
        >
          <v-list dense>
            <template v-for="item in items">
              <v-row
                v-if="item.heading"
                :key="item.heading"
                align="center"
              >
                <v-col cols="6">
                  <v-subheader v-if="item.heading">
                    {{ item.heading }}
                  </v-subheader>
                </v-col>
                <v-col
                  cols="6"
                  class="text-center"
                >
                  <a
                    href="#!"
                    class="body-2 black--text"
                  ></a>
                </v-col>
              </v-row>
              <v-list-group
                v-else-if="item.children"
                :key="item.text"
                v-model="item.model"
                :prepend-icon="item.model ? item.icon : item['icon-alt']"
                color="#24324f"
                append-icon=""
              >
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ item.text }}
                    </v-list-item-title>
                  </v-list-item-content>
                </template>
                <v-list-item
                  v-for="(child, i) in item.children"
                  :key="i"
                  link
                  router :to="child.route"
                >
                  <v-list-item-action v-if="child.icon" class="ml-5">
                    <v-icon class="mr-1">{{ child.icon }}</v-icon>
                  </v-list-item-action>
                  <v-list-item-content >
                    <v-list-item-title>
                      {{ child.text }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-group>
              <v-list-item
                v-else
                :key="item.text"
                link
                router :to="link.route"
              >
                <v-list-item-action>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>
                    {{ item.text }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list>
        </v-navigation-drawer>
    </v-container>
</template>
<script>
export default {
  data: () => ({
    drawer: null,
    selectedSearch: 'resource',
    search: '',
    validSearch: true
  }),
  computed: {
    items: function () {
        return ([
          {
            icon: 'mdi-chevron-up',
            'icon-alt': 'mdi-chevron-down',
            text: 'Users',
            model: true,
            children: [
              { text: 'All Users', icon: 'mdi-account-multiple', route: '/droots/users' },
              { text: 'Administrators', icon: 'mdi-account-multiple', route: '/droots/administrators' },
            //   { text: 'Events Archive', icon: 'mdi-history', route: '/events/alleventsarchive' },
            //   { text: 'Deleted Events', icon: ' mdi-calendar-remove ', route: '/events/alldeletedevents' },
            //   { text: 'My Events ', icon: 'mdi-calendar', route: '/events/myevents' }
            ]
          },
          {
            icon: 'mdi-chevron-up',
            'icon-alt': 'mdi-chevron-down',
            text: 'Resources',
            model: true,
            children: [
              { text: 'Resources', icon: 'mdi-database', route: '/droots/resources/all' },
              { text: 'Ice', icon: 'mdi-cube-outline', route: '/droots/resources/ice' },
              { text: 'Water', icon: 'mdi-water', route: '/droots/resources/water' },
              { text: 'Food', icon: 'mdi-food-variant', route: '/droots/resources/food' },
              { text: 'Clothing', icon: 'mdi-hanger', route: '/droots/resources/clothing' },
              { text: 'Tools', icon: 'mdi-package-variant', route: '/droots/resources/tools' },
              { text: 'Health', icon: 'mdi-hospital', route: '/droots/resources/health' },
              { text: 'Power Resources', icon: 'mdi-power', route: '/droots/resources/powerresources' },
              { text: 'Fuel', icon: 'mdi-gas-station', route: '/droots/resources/fuel' },
              { text: 'Heavy Equipmet', icon: ' mdi-weight', route: '/droots/resources/heavyequipment' },
              { text: 'Batteries', icon: ' mdi-battery', route: '/droots/resources/batteries' },
            //   { text: 'Ice', icon: 'mdi-tag-multiple', route: '/tagsmanagement' },
            //   { text: 'Coordinates Management', icon: 'mdi-map-marker-radius', route: '/roomscoordinatesmanagement' }
            ]
          },
        //   {
        //     icon: 'mdi-chevron-up',
        //     'icon-alt': 'mdi-chevron-down',
        //     text: 'Privilege Management',
        //     model: true,
        //     children: [
        //       // { text: 'Privilege Management', icon: 'mdi-account-key-outline', route: '/privilegemanagement/eventcreators' },
        //       { text: 'Moderators', icon: 'mdi-account-key-outline', route: '/privilegemanagement/moderators' },
        //       { text: 'Event creators', icon: 'mdi-account-key-outline', route: '/privilegemanagement/eventcreators' }
        //     ]
        //   }
        ])
    }
  },
  mounted () {
    if (this.$route.name === 'search') {
      this.search = this.$route.params.keyword
    }
  },
  methods: {
    followRoute: function () {
      if ((this.selectedSearch !== this.$route.params.searchtype && this.search !== this.$route.params.keyword) && (this.$route.params.keyword !== 'null' && this.search.trim() !== '')) {
        this.$router.push({ name: 'search', params: { searchtype: this.selectedSearch, keyword: (this.search.trim() === '' ? 'null' : this.search) } })
      }
    },
    clearValdation: function () {
      this.$refs.searchForm.resetValidation()
    }
  },
  watch: {
    search: function () {
      if ((this.$route.params.keyword !== 'null' || this.search.trim() !== '') && (this.$route.name === 'search')) {
        this.selectedSearch = this.$route.params.searchtype
        this.$router.push({ name: 'search', params: { searchtype: this.selectedSearch, keyword: (this.search.trim() === '' ? 'null' : this.search) } })
      }
    },
    selectedSearch: function () {
      if ((this.$route.name === 'search')) {
        // this.selectedSearch = this.$route.params.searchtype
        this.$router.push({ name: 'search', params: { searchtype: this.selectedSearch, keyword: (this.search.trim() === '' ? 'null' : this.search) } })
      }
    },
    $route: function () {
      if ((this.$route.name === 'search')) {
        // this.selectedSearch = this.$route.params.searchtype
        this.selectedSearch = this.$route.params.searchtype
      }
    }
  },
  directives: {
    'click-outside': {
      bind: function (el, binding, vNode) {
        // Provided expression must evaluate to a function.
        if (typeof binding.value !== 'function') {
          const compName = vNode.context.name
          let warn = `[Vue-click-outside:] provided expression '${binding.expression}' is not a function, but has to be`
          if (compName) { warn += `Found in component '${compName}'` }
          console.warn(warn)
        }
        // Define Handler and cache it on the element
        const bubble = binding.modifiers.bubble
        const handler = (e) => {
          if (bubble || (!el.contains(e.target) && el !== e.target)) {
            binding.value(e)
          }
        }
        el.__vueClickOutside__ = handler
        // add Event Listeners
        document.addEventListener('click', handler)
      },
    //   unbind: function (el, binding) {
    //     // Remove Event Listeners
    //     document.removeEventListener('click', el.__vueClickOutside__)
    //     el.__vueClickOutside__ = null
    //   }
    }
  }
}
</script>