"""Generate docs for the Edward API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

import edward as ed

from tensorflow.python import debug as tf_debug
from tensorflow.python.util import tf_inspect
import generate_lib

if __name__ == '__main__':
  doc_generator = generate_lib.DocGenerator()
  doc_generator.add_output_dir_argument()
  doc_generator.add_src_dir_argument()

  # This doc generator works on the TensorFlow codebase. Since this script lives
  # at docs/parser, and all code is defined somewhere inside
  # edward/, we can compute the base directory (two levels up), which is
  # valid unless we're trying to apply this to a different code base, or are
  # moving the script around.
  script_dir = os.path.dirname(tf_inspect.getfile(tf_inspect.currentframe()))
  default_base_dir = os.path.join(script_dir, '..', '..', 'edward')
  doc_generator.add_base_dir_argument(default_base_dir)

  flags = doc_generator.parse_known_args()

  doc_generator.set_py_modules([('ed', ed)])

  doc_generator.set_do_not_descend_map({
      #  TODO
      'ed.criticisms.ppc_plots': [
          'sns',
      ],
      'ed': [
          'inferences',
          'models',
          'util',
      ],
      'ed.inferences.bigan_inference': [
          'six',
          'tf',
      ],
      'ed.inferences.conjugacy.conjugacy': [
          'np',
          'six',
          'tf',
      ],
      'ed.inferences.conjugacy.conjugate_log_probs': [
          'np',
          'tf',
      ],
      'ed.inferences.conjugacy': [
          'np',
          'six',
          'tf',
      ],
      'ed.inferences.conjugacy.simplify': [
          'np',
          'tf',
      ],
  })

  sys.exit(doc_generator.build(flags))
