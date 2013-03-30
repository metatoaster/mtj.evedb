import unittest
import doctest


def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite(
            'README.rst', package='mtj.evedb',
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
        ),

    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
