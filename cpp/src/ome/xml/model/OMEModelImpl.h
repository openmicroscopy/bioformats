/*
 * #%L
 * OME-XML C++ library for working with OME-XML metadata structures.
 * %%
 * Copyright © 2006 - 2013 Open Microscopy Environment:
 *   - Massachusetts Institute of Technology
 *   - National Institutes of Health
 *   - University of Dundee
 *   - Board of Regents of the University of Wisconsin-Madison
 *   - Glencoe Software, Inc.
 * %%
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 * 
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 * 
 * The views and conclusions contained in the software and documentation are
 * those of the authors and should not be interpreted as representing official
 * policies, either expressed or implied, of any organization.
 * #L%
 */

#ifndef OME_XML_MODEL_OMEMODELIMPL_H
#define OME_XML_MODEL_OMEMODELIMPL_H

#include <ome/xml/model/OMEModel.h>
#include <ome/xml/model/OMEModelObject.h>

namespace ome
{
  namespace xml
  {
    namespace model
    {

      class OMEModelImpl : public OMEModel
      {
      public:
	OMEModelImpl ();

        ~OMEModelImpl ();

      private:
	typedef std::map<std::string, OMEModelObject::shared_ptr> object_map_type;
	typedef std::map<OMEModelObject::shared_ptr, std::vector<Reference> > reference_map_type;

	object_map_type modelObjects;
	reference_map_type references;

      public:
	OMEModelObject::shared_ptr
	removeModelObject(const std::string& id);

	OMEModelObject::shared_ptr
	addModelObject(const std::string& id,
		       OMEModelObject::shared_ptr& object);

	OMEModelObject::shared_ptr
	getModelObject(const std::string& id) const;

	const object_map_type&
	getModelObjects () const;

	bool
	addReference (OMEModelObject::shared_ptr& a,
		      Reference::shared_ptr& b);

	const reference_map_type&
	getReferences ();

	int
	resolveReferences ();

      };

    }
  }
}

#endif // OME_XML_MODEL_OMEMODELIMPL_H

/*
 * Local Variables:
 * mode:C++
 * End:
 */
