Quickstart
----------

Using CLI
^^^^^^^^^

To capture actions
==================

.. code-block:: bash

   replay-wizard capture openyoutube

To replay actions
=================

.. code-block:: bash

   replay-wizard replay openyoutube -d 10

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
