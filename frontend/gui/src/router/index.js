import Vue from 'vue'
import VueRouter from 'vue-router'
import Users from '../components/Users.vue'
import Administrators from '../components/Administrators.vue'
import Resources from '../components/Resources.vue'
import Food from '../components/Food.vue'
import Ice from '../components/Ice.vue'
import Water from '../components/Water.vue'
import Clothing from '../components/Clothing.vue'
import Tools from '../components/Tools.vue'
import Health from '../components/Health.vue'
import PowerResources from '../components/PowerResources.vue'
import Fuel from '../components/Fuel.vue'
import HeavyEquipment from '../components/HeavyEquipment.vue'
import Batteries from '../components/Batteries.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/droots/users',
        name: 'all users',
        component: Users
    },
    {
        path: '/droots/administrators',
        name: 'administrators',
        component: Administrators
    },
    {
        path: '/droots/resources/all',
        name: 'resources',
        component: Resources
    },
    {
        path: '/droots/resources/food',
        name: 'food',
        component: Food
    },
    {
        path: '/droots/resources/ice',
        name: 'ice',
        component: Ice
    },
    {
        path: '/droots/resources/water',
        name: 'water',
        component: Water
    },
    {
        path: '/droots/resources/clothing',
        name: 'clothing',
        component: Clothing
    },
    {
        path: '/droots/resources/tools',
        name: 'tools',
        component: Tools
    },
    {
        path: '/droots/resources/health',
        name: 'health',
        component: Health
    },
    {
        path: '/droots/resources/powerresources',
        name: 'power resources',
        component: PowerResources
    },
    {
        path: '/droots/resources/fuel',
        name: 'fuel',
        component: Fuel
    },
    {
        path: '/droots/resources/heavyequipment',
        name: 'heavyequipment',
        component: HeavyEquipment
    },
    {
        path: '/droots/resources/Batteries',
        name: 'batteries',
        component: Batteries
    },
]


const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  export default router