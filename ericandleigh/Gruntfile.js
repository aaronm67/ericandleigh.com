module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        mangle: false
      },
      dist: {
        files: {
          'media/min.js': ["media/js/jquery-1.6.js", "media/js/cufon-yui.js", "media/js/cufon-replace.js", "media/js/Josefin_Sans_400.font.js", "media/js/Tangerine_700.font.js", "media/js/atooltip.jquery.js", "media/js/jquery.nivo.slider.pack.js", "media/js/script.js"],
        }
      }
    },
	concat: {
		dist: {
			src: [ "media/css/reset.css", "media/css/layout.css", "media/css/style.css" ],
			dest: "media/css/min.css"
		}
	}

  });


  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.registerTask('default', ['uglify', 'concat' ]);
};

