.. DV Flow IDE Library documentation master file, created by
   sphinx-quickstart on Sun May 11 13:54:28 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

###################
DV Flow IDE Library
###################

The DV Flow IDE library provides tasks for maintaining source configurations
for various IDE plug-ins. The tasks focus on IDE plug-ins for working with
HDL descriptions, since these tend to require more configuration that other
programming languages.

.. contents::
    :depth: 2

Task: UpdateFileList
====================

The UpdatefileList task produces a file list corresponding to the input
files provided by the dependent tasks.

Consumes
--------

* **systemVerilogSource**
* **verilogSource**

Produces
--------

Parameters
----------

* **uvm** - [Optional] Boolean variable that controls whether the UVM library is enabled.



Supported Tools
===============
Tasks to support a specific tools are in named packages. For example, the
package to support Verible is named `ide.vbl`.

* **dvt** - Tasks to support AMIQ DVT
* **vbl** - Tasks to support Verible



