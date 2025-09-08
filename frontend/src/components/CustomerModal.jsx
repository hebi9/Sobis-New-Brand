import React, { useState } from 'react';

const CustomerModal = ({ isOpen, onClose, customer, onUpdate }) => {
  const [form, setForm] = useState(customer || {});
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const saveCustomer = async () => {
    setLoading(true);
    try {
      const res = await fetch(`/api/customers/${customer.id}/`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(form),
      });
      const updated = await res.json();
      onUpdate(updated);
      onClose();
    } catch (err) {
      alert('Error al actualizar cliente');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="modal-backdrop">
      <div className="modal">
        <h2>Editar cliente</h2>
        <input
          name="name"
          value={form.name || ''}
          onChange={handleChange}
          placeholder="Nombre"
        />
        <input
          name="email"
          value={form.email || ''}
          onChange={handleChange}
          placeholder="Correo"
        />
        <input
          name="phone"
          value={form.phone || ''}
          onChange={handleChange}
          placeholder="Teléfono"
        />
        <div>
          <button onClick={saveCustomer} disabled={loading}>
            {loading ? 'Guardando...' : 'Guardar'}
          </button>
          <button onClick={onClose} style={{ marginLeft: '10px' }}>
            Cancelar
          </button>
        </div>
      </div>
    </div>
  );
};

export default CustomerModal;
