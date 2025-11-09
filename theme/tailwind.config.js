module.exports = {
  content: [
    './templates/**/*.html',
    '../app/templates/**/*.html',
    '../cars/templates/**/*.html',
    '../account/templates/**/*.html',
    '../**/templates/**/*.html',
    '../../**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
}
