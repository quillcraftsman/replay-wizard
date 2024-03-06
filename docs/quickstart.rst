Quickstart
----------

Using CLI
^^^^^^^^^

To capture actions
==================

.. code-block:: bash

   wizard-capture openyoutube

To replay actions
=================

.. code-block:: bash

   wizard-replay openyoutube -d 10

To combine sequences
=================

.. code-block:: bash

   wizard-combine three one two

Using python
^^^^^^^^^^^^

To capture actions
==================

.. literalinclude:: ../quickstart/capturing.py
   :pyobject: capture_actions

To replay actions
=================

.. literalinclude:: ../quickstart/replay.py
   :pyobject: replay_actions
