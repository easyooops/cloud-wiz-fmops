import { useAuthStore } from '@/store/auth';

export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore();

    const publicPaths = ['/login'];

    console.log('== GoogleDriveCallback() =============================');
    console.log(authStore.isAuthenticated);
    console.log(to.path);

    if (!authStore.isAuthenticated && !publicPaths.includes(to.path)) {
      return navigateTo('/login');
    }
});