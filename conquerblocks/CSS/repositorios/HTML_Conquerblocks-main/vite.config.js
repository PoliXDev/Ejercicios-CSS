import { defineConfig } from 'vite';
import { resolve } from 'path';
import { glob } from 'glob';
import { fileURLToPath } from 'url';


const htmlPages = {};
const pages = glob.sync('./*.html');

pages.forEach(page => {
  const basename = page.split('/').pop();
  htmlPages[basename.replace('.html', '')] = resolve(__dirname, page);
});

export default defineConfig({
  base: '/HTML_Conquerblocks/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        blog: resolve(__dirname, 'blog.html'),
        contacto: resolve(__dirname, 'contacto.html'),
        cursos: resolve(__dirname, 'cursos.html'),
        login: resolve(__dirname, 'login.html'),
        registro: resolve(__dirname, 'registro.html'),
        'quienes-somos': resolve(__dirname, 'quienes-somos.html'),
        'curso_blockchain': resolve(__dirname, 'curso_blockchain.html'),
        'curso_fullstack': resolve(__dirname, 'curso_fullstack.html'),
        'curso_inteligencia_artificial': resolve(__dirname, 'curso_inteligencia_artificial.html'),
        'aviso-legal': resolve(__dirname, 'aviso-legal.html')
      },
      output: {
        manualChunks: undefined,
      },
    },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, './src'),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        
      },
    },
  },
  server: {
    port: 3000,
    open: true
  },
  plugins: []
});

