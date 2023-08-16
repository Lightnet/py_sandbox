// vite.config.ts
// https://vitejs.dev/guide/build.html
import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';

export default defineConfig({
  plugins: [solidPlugin()],
  build:{
    watch:true
  }
});