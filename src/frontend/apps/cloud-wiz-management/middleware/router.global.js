import { useAuthStore } from '@/store/auth';

export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore();

    const publicPaths = ['/login'];

    // Check if the request path is /google/callback
    if (!authStore.isAuthenticated && '/google/callback'.includes(to.path)) {
      // Get the full path including query parameters
      const fullPath = to.fullPath;
      const url = import.meta.env.VITE_MANAGEMENT_URL;
      console.log(fullPath);
      console.log(url);
      console.log(`${url}${fullPath}`);
      // Redirect to the same path on the new domain
      return navigateTo(`${url}${fullPath}`, { external: true });
    }


    if (!authStore.isAuthenticated && !publicPaths.includes(to.path)) {
      return navigateTo('/login');
    }
});