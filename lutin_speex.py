#!/usr/bin/python
import lutinModule as module
import lutinTools as tools

def get_desc():
	return "speex dsp : Algorithm of speex codec"


def create(target):
	myModule = module.Module(__file__, 'speex', 'LIBRARY')
	# add extra compilation flags :
	myModule.add_extra_compile_flags()
	# add the file to compile:
	myModule.add_src_file([
		'libspeex/bits.c',
		'libspeex/exc_5_256_table.c',
		'libspeex/gain_table_lbr.c',
		'libspeex/kiss_fftr.c',
		'libspeex/modes.c',
		'libspeex/smallft.c',
		'libspeex/vq.c',
		'libspeex/cb_search.c',
		'libspeex/exc_5_64_table.c',
		'libspeex/hexc_10_32_table.c',
		'libspeex/lpc.c',
		'libspeex/modes_wb.c',
		'libspeex/speex.c',
		'libspeex/window.c',
		'libspeex/exc_10_16_table.c',
		'libspeex/exc_8_128_table.c',
		'libspeex/hexc_table.c',
		'libspeex/lsp.c',
		'libspeex/nb_celp.c',
		'libspeex/speex_callbacks.c',
		'libspeex/exc_10_32_table.c',
		'libspeex/filters.c',
		'libspeex/high_lsp_tables.c',
		'libspeex/lsp_tables_nb.c',
		'libspeex/quant_lsp.c',
		'libspeex/speex_header.c',
		'libspeex/vbr.c',
		'libspeex/exc_20_32_table.c',
		'libspeex/gain_table.c',
		'libspeex/kiss_fft.c',
		'libspeex/ltp.c',
		'libspeex/sb_celp.c',
		'libspeex/stereo.c',
		'libspeex/vorbis_psy.c'
		])
	
	# name of the dependency
	#myModule.add_module_depend('speexdsp')
	
	myModule.compile_version_CC(1989, gnu=True)
	myModule.add_export_path(tools.get_current_path(__file__) + "/include")
	# configure library :
	
	# Make use of ARM4 assembly optimizations
	#myModule.compile_flags_CC("-DARM4_ASM=1")
	# Make use of ARM5E assembly optimizations
	#myModule.compile_flags_CC("-DARM5E_ASM=1")
	# Make use of Blackfin assembly optimizations
	#myModule.compile_flags_CC("-DBFIN_ASM=1")
	# Disable all parts of the API that are using floats
	#myModule.compile_flags_CC("-DDISABLE_FLOAT_API=1")
	# Enable valgrind extra checks
	#myModule.compile_flags_CC("-DENABLE_VALGRIND=1")
	# Symbol visibility prefix */
	#define EXPORT __attribute__((visibility("default")))
	myModule.compile_flags_CC("-DEXPORT=''")
	# Debug fixed-point implementation */
	#myModule.compile_flags_CC("-DFIXED_DEBUG=1")
	# Compile as fixed-point / floating-point
	if True:
		myModule.compile_flags_CC("-DFIXED_POINT")
	else:
		myModule.compile_flags_CC("-DFLOATING_POINT")
		# Enable NEON support */
		#myModule.compile_flags_CC("-D_USE_NEON=1")
		# Enable SSE support */
		myModule.compile_flags_CC("-D_USE_SSE=1")
		# Enable SSE2 support */
		myModule.compile_flags_CC("-D_USE_SSE2=1")
	# Define to 1 if you have the <alloca.h> header file.
	myModule.compile_flags_CC("-DHAVE_ALLOCA_H=1")
	# Use FFT from OggVorbis */
	myModule.compile_flags_CC("-DUSE_SMALLFT=1")
	# Use C99 variable-size arrays */
	myModule.compile_flags_CC("-DVAR_ARRAYS=1")
	
	return myModule


